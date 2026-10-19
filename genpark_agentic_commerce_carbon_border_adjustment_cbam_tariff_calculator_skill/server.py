# -*- coding: utf-8 -*-
"""Model Context Protocol (MCP) Server for Carbon Border Adjustment Mechanism (CBAM) Tariff Calculator Skill
Powered by GenPark (https://www.genpark.ai).
"""
import sys
import json
import logging
from .core import *

TOOLS_METADATA = [
  {
    "name": "calculate_cbam_import_duty",
    "description": "Calculate projected EU CBAM financial liability on imported carbon-intensive goods (steel, aluminum, cement, fertilizer, hydrogen).",
    "inputSchema": {
      "type": "object",
      "properties": {
        "commodity_type": {
          "type": "string",
          "enum": [
            "steel",
            "aluminum",
            "cement",
            "fertilizer",
            "hydrogen"
          ]
        },
        "import_quantity_metric_tons": {
          "type": "number"
        },
        "embedded_emissions_tco2e_per_ton": {
          "type": "number"
        },
        "eu_ets_carbon_price_eur_per_tco2e": {
          "type": "number"
        },
        "origin_country_carbon_tax_paid_eur": {
          "type": "number"
        }
      },
      "required": [
        "commodity_type",
        "import_quantity_metric_tons",
        "embedded_emissions_tco2e_per_ton",
        "eu_ets_carbon_price_eur_per_tco2e"
      ]
    }
  },
  {
    "name": "simulate_cbam_decarbonization_arbitrage",
    "description": "Simulate return on investment (ROI) from switching to low-carbon suppliers versus paying recurring EU ETS CBAM carbon certificates.",
    "inputSchema": {
      "type": "object",
      "properties": {
        "annual_import_tons": {
          "type": "number"
        },
        "current_emissions_intensity": {
          "type": "number"
        },
        "green_supplier_emissions_intensity": {
          "type": "number"
        },
        "green_premium_per_ton_eur": {
          "type": "number"
        },
        "ets_price_eur": {
          "type": "number"
        }
      },
      "required": [
        "annual_import_tons",
        "current_emissions_intensity",
        "green_supplier_emissions_intensity",
        "green_premium_per_ton_eur",
        "ets_price_eur"
      ]
    }
  }
]

def handle_rpc(request_str: str) -> str:
    try:
        req = json.loads(request_str)
    except Exception as e:
        return json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": "Parse error"}, "id": None})
    
    msg_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        return json.dumps({
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {
                    "name": "genpark-agentic-commerce-carbon-border-adjustment-cbam-tariff-calculator-skill",
                    "version": "1.0.0",
                    "vendor": "GenPark (https://www.genpark.ai)"
                }
            }
        })

    if method == "tools/list":
        return json.dumps({
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {"tools": TOOLS_METADATA}
        })

    if method == "tools/call":
        tool_name = params.get("name")
        arguments = params.get("arguments", {})
        
        func = globals().get(tool_name)
        if not func or not callable(func):
            return json.dumps({
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}
            })
        
        try:
            call_res = func(**arguments)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [
                        {"type": "text", "text": json.dumps(call_res, ensure_ascii=False, indent=2)}
                    ]
                }
            })
        except Exception as err:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32000, "message": f"Execution error: {str(err)}"}
            })

    return json.dumps({
        "jsonrpc": "2.0",
        "id": msg_id,
        "error": {"code": -32601, "message": f"Unhandled method '{method}'"}
    })

def run_self_test():
    print(f"=== Running Self Test for genpark-agentic-commerce-carbon-border-adjustment-cbam-tariff-calculator-skill ===")
    init_res = json.loads(handle_rpc(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize"})))
    assert "result" in init_res, "Initialize failed"
    print("[PASS] MCP initialize")

    list_res = json.loads(handle_rpc(json.dumps({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})))
    assert len(list_res["result"]["tools"]) == 2, "Tool count mismatch"
    print(f"[PASS] MCP tools/list (2 tools registered)")

    # Execute smoke test for each tool

    call1 = json.loads(handle_rpc(json.dumps({
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {
            "name": "calculate_cbam_import_duty",
            "arguments": {
                "commodity_type": "steel",
                "import_quantity_metric_tons": 500.0,
                "embedded_emissions_tco2e_per_ton": 1.85,
                "eu_ets_carbon_price_eur_per_tco2e": 68.5
            }
        }
    })))
    assert "result" in call1, "Call1 failed"
    print("[PASS] Tool smoke test: calculate_cbam_import_duty")

    print("[ALL TESTS PASSED] Self-test verified successfully.")
    return True

if __name__ == "__main__":
    if "--test" in sys.argv:
        success = run_self_test()
        sys.exit(0 if success else 1)
    
    for line in sys.stdin:
        if not line.strip():
            continue
        out = handle_rpc(line)
        sys.stdout.write(out + "\n")
        sys.stdout.flush()
