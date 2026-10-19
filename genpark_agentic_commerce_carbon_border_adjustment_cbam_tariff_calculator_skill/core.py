# -*- coding: utf-8 -*-
"""CBAM Carbon Tariff Calculator Skill for GenPark Agentic Commerce."""
import json
from typing import Dict, Any

def calculate_cbam_import_duty(commodity_type: str, import_quantity_metric_tons: float, embedded_emissions_tco2e_per_ton: float, eu_ets_carbon_price_eur_per_tco2e: float, origin_country_carbon_tax_paid_eur: float = 0.0) -> Dict[str, Any]:
    total_embedded_emissions_tco2e = round(import_quantity_metric_tons * embedded_emissions_tco2e_per_ton, 2)
    gross_cbam_liability_eur = round(total_embedded_emissions_tco2e * eu_ets_carbon_price_eur_per_tco2e, 2)

    # Deduction for carbon price legitimately paid in origin jurisdiction
    net_cbam_duty_eur = round(max(0.0, gross_cbam_liability_eur - origin_country_carbon_tax_paid_eur), 2)
    effective_tariff_per_ton_eur = round(net_cbam_duty_eur / max(0.001, import_quantity_metric_tons), 2)

    return {
        "commodity": commodity_type.upper(),
        "import_volume_tons": import_quantity_metric_tons,
        "emissions_intensity_factor": embedded_emissions_tco2e_per_ton,
        "total_embedded_carbon_tco2e": total_embedded_emissions_tco2e,
        "benchmark_eu_ets_price_eur": eu_ets_carbon_price_eur_per_tco2e,
        "gross_cbam_obligation_eur": gross_cbam_liability_eur,
        "origin_country_credit_eur": origin_country_carbon_tax_paid_eur,
        "net_payable_cbam_tariff_eur": net_cbam_duty_eur,
        "unit_cbam_surcharge_per_ton_eur": effective_tariff_per_ton_eur,
        "regulatory_framework": "Regulation (EU) 2023/956 Carbon Border Adjustment Mechanism",
        "auditor": "GenPark Cross-Border Trade & Climate Sentinel"
    }

def simulate_cbam_decarbonization_arbitrage(annual_import_tons: float, current_emissions_intensity: float, green_supplier_emissions_intensity: float, green_premium_per_ton_eur: float, ets_price_eur: float) -> Dict[str, Any]:
    current_cbam_cost = annual_import_tons * current_emissions_intensity * ets_price_eur
    green_cbam_cost = annual_import_tons * green_supplier_emissions_intensity * ets_price_eur
    cbam_duty_saved_eur = round(current_cbam_cost - green_cbam_cost, 2)

    total_green_procurement_premium_eur = round(annual_import_tons * green_premium_per_ton_eur, 2)
    net_annual_arbitrage_gain_eur = round(cbam_duty_saved_eur - total_green_procurement_premium_eur, 2)

    if net_annual_arbitrage_gain_eur > 0:
        decision = "SWITCH_TO_GREEN_SUPPLIER"
        rationale = f"Switching to green supplier saves €{net_annual_arbitrage_gain_eur:,.2f} net after accounting for procurement premium."
    else:
        decision = "RETAIN_CONVENTIONAL_AND_PAY_TARIFF"
        rationale = f"Green procurement premium exceeds CBAM carbon certificate liabilities by €{abs(net_annual_arbitrage_gain_eur):,.2f}."

    return {
        "annual_volume_tons": annual_import_tons,
        "annual_cbam_tax_avoided_eur": cbam_duty_saved_eur,
        "annual_supplier_premium_cost_eur": total_green_procurement_premium_eur,
        "net_annual_arbitrage_surplus_eur": net_annual_arbitrage_gain_eur,
        "strategic_recommendation": decision,
        "economic_rationale": rationale
    }
