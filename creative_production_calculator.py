#!/usr/bin/env python3
"""
E-Commerce Ad Creative Production Cost & Scaling Estimator 2026.
Calculates agency outsourcing rates vs AI-assisted batch asset generation.
"""
import argparse

def calculate_production(creatives_per_month, agency_unit_rate, adcreative_sub):
    agency_monthly = creatives_per_month * agency_unit_rate
    ai_monthly = adcreative_sub
    monthly_savings = agency_monthly - ai_monthly
    unit_cost_ai = ai_monthly / creatives_per_month if creatives_per_month > 0 else 0.0
    return {
        "creatives_per_month": creatives_per_month,
        "agency_monthly": agency_monthly,
        "ai_monthly": ai_monthly,
        "monthly_savings": monthly_savings,
        "unit_cost_ai": unit_cost_ai
    }

def main():
    parser = argparse.ArgumentParser(description="E-Commerce Creative Production Cost Estimator")
    parser.add_argument("--creatives-per-month", type=int, default=50, help="Monthly creative variants required (default: 50)")
    parser.add_argument("--agency-unit-rate", type=float, default=45.0, help="Agency cost per ad creative in USD (default: $45.00)")
    parser.add_argument("--adcreative-sub", type=float, default=149.0, help="AdCreative.ai monthly fee in USD (default: $149.00)")
    args = parser.parse_args()

    res = calculate_production(args.creatives_per_month, args.agency_unit_rate, args.adcreative_sub)
    print(f"Monthly Asset Volume:    {res['creatives_per_month']} ad variants")
    print(f"Agency Outsourced Total: ${res['agency_monthly']:.2f}/mo")
    print(f"AI-Assisted Total Cost:  ${res['ai_monthly']:.2f}/mo")
    print(f"Monthly Net Savings:     ${res['monthly_savings']:.2f}/mo")
    print(f"Production Cost Per Unit:${res['unit_cost_ai']:.2f}/asset")

if __name__ == "__main__":
    main()
