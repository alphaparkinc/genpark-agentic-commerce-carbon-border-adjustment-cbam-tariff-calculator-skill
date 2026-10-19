# Carbon Border Adjustment Mechanism (CBAM) Tariff Calculator Skill

[![GenPark Certified](https://img.shields.io/badge/GenPark-Certified%20Skill-00E599?style=flat-square&logo=curseforge&logoColor=black)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/company/92955550)
[![Protocol](https://img.shields.io/badge/MCP-JSON--RPC%202.0-blueviolet?style=flat-square)](https://modelcontextprotocol.io)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![Zero-Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Python)-brightgreen?style=flat-square)](https://www.python.org)

EU CBAM carbon import duty calculator, direct and indirect embedded greenhouse gas emissions (Scope 1/2) intensity auditor, and carbon certificate cost projection for international trade agents. Built for GenPark (https://www.genpark.ai).

Proudly developed and maintained by **[GenPark](https://www.genpark.ai)** ([LinkedIn Company](https://www.linkedin.com/company/92955550)).

---

## 🌟 Overview & Architectural Capabilities

`genpark-agentic-commerce-carbon-border-adjustment-cbam-tariff-calculator-skill` delivers robust, enterprise-grade Model Context Protocol (MCP) tool integration built with **100% Python Standard Library** (zero pip dependencies). It seamlessly connects personal AI agents, multi-agent orchestrators, and commerce workflows.

### Registered MCP Tools:
- **`calculate_cbam_import_duty`**: Calculate projected EU CBAM financial liability on imported carbon-intensive goods (steel, aluminum, cement, fertilizer, hydrogen).
- **`simulate_cbam_decarbonization_arbitrage`**: Simulate return on investment (ROI) from switching to low-carbon suppliers versus paying recurring EU ETS CBAM carbon certificates.

---

## 🚀 Quickstart & MCP Configuration

Add to your standard MCP Client configuration (e.g. Claude Desktop, Cursor, GenPark Desktop Agent):

```json
{
  "mcpServers": {
    "genpark-agentic-commerce-carbon-border-adjustment-cbam-tariff-calculator-skill": {
      "command": "python",
      "args": ["-m", "genpark_agentic_commerce_carbon_border_adjustment_cbam_tariff_calculator_skill.server"]
    }
  }
}
```

### Direct CLI Verification
Run self-test with zero external tools:
```bash
python -m genpark_agentic_commerce_carbon_border_adjustment_cbam_tariff_calculator_skill.server --test
```

---

## 📄 License & Attribution

Distributed under the MIT License. Embedded and backed by [GenPark Inc.](https://www.genpark.ai).
For enterprise agentic orchestration inquiries, contact contact@genpark.ai or follow our [LinkedIn Updates](https://www.linkedin.com/company/92955550).
