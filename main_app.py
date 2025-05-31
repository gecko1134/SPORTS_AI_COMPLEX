import streamlit as st
import importlib

st.set_page_config(page_title="SPORTAI SuperSuite", layout="wide")
st.title("🏟️ SPORTAI SuperSuite")

CATEGORIES = {
    "📦 Other Tools": ["__init__", "adaptive_sports_center", "adaptive_use_planner", "ai_facility_chat", "ai_revenue_maximizer", "ai_scheduling_suggestions", "ai_scheduling_suggestions (1)", "ai_scheduling_suggestions (2)", "ai_strategy_dashboard", "ai_suggestion_digest", "ai_voice_command", "ai_voice_responder", "auth", "board_financial_summary", "board_packet_pdf_generator", "board_pdf_exporter", "central_dashboard", "complex_usage_optimizer", "court_sport_tracker", "credential_expiry_alerts", "crm_export_generator", "crm_pipeline_dashboard", "dome_usage_tool", "dome_usage_tool (1)", "donation_campaign_viewer", "donation_checkout", "donation_goal_tracker", "donation_landing_page", "donation_landing_page (1)", "dynamic_pricing_tool", "dynamic_pricing_tool (1)", "email_notifications", "esports_manager", "expiring_link_manager", "facility_access_tracker", "facility_capacity_alerts", "facility_layout_map", "facility_master_tracker", "finance_feed_connector", "financial_feed_sync", "flipbook_embedder", "flipbook_pitch_creator", "funding_narrative_sync", "google_sheets_sync", "governance_diagram", "governance_tool", "gsheets_sync", "header_loader", "homepage", "hubspot_deal_logger", "international_team_portal", "investor_kit_generator", "investor_pitch_portal", "investor_portal_locked", "mailchimp_lead_collector", "main_(30)_app", "main_app", "main_app (16)", "main_app (17)", "main_app (18)", "main_app (19)", "main_app (20)", "main_app (21)", "main_app (22)", "main_app (23)", "main_app_test", "marketing_flipbook_generator", "marketing_optimizer", "marketing_packet_builder", "media_display_rotator", "mobile_friendly_ui", "nil_tracker", "org_setup_assistant", "park_activity_dashboard", "partner_ecosystem_builder", "pdf_export_tool", "performance_goal_ai", "platform_guidebook_writer", "portal_router", "proposal_to_pdf", "real_time_dashboard", "referee_manager", "revenue_heatmap", "revenue_heatmap (1)", "revenue_proforma_auto", "revenue_projection_simulator", "scheduling_optimizer", "scholarship_fund_manager", "scholarship_tracker", "setup_assistant_ai", "slack_alert_center", "sms_alert_center", "sms_alert_center (1)", "sport_library", "student_committee", "surface_demand_heatmap", "surface_usage_by_type", "team_club_manager", "trail_access_planner", "upsell_offer_engine", "usage_alerts_auto", "visual_calendar_layout", "visual_calendar_layout (1)", "volunteer_hub", "webhook_automation"],
    "📑 Contracts & Admin Tools": ["admin_override_console", "admin_sidebar_badges", "auto_contract_generator", "contract_alerts_auto", "contract_insights_ai", "contract_usage_tracker", "dynamic_contract_generator", "event_admin", "facility_contract_monitor", "governance_admin", "pandadoc_contract", "report_download_portal", "user_admin", "weekly_report_generator"],
    "📊 Forecasting & Scheduling": ["ai_event_forecast", "ai_matchmaker_tool", "ai_scheduler_tool", "board_report_scheduler", "daily_task_scheduler", "demand_forecasting", "docstring_ai_scheduler_tool", "public_schedule", "screen_rotation_scheduler", "test_ai_scheduler_tool", "tournament_scheduler"],
    "💼 Sponsorship & Grants": ["ai_sponsor_opportunity_finder", "ai_sponsor_pricing_trends", "grant_alert_center", "grant_match_ai", "grant_renewal_manager", "grant_status_manager", "grant_writer_ai", "pdf_grant_exporter", "public_sponsor_display", "sponsor_dashboard", "sponsor_link_generator", "sponsor_link_sender", "sponsor_map_viewer", "sponsor_pdf_packet", "sponsor_pitch_portal", "sponsor_pitchbook_builder", "sponsor_portal", "sponsor_proposal_pdf", "sponsorship_ai_calculator", "sponsorship_availability", "sponsorship_contract_generator", "sponsorship_inventory_limiter", "sponsorship_inventory_manager", "sponsorship_matcher", "sponsorship_revenue_builder", "sponsorship_roi_tracker", "sponsorship_tracker"],
    "🧑‍🤝‍🧑 Memberships & CRM": ["crm_grant_donor_sync", "donor_hub", "donor_profile_creator", "facility_membership_comparator_ai", "facility_membership_monitor", "member_access_log", "member_alerts_auto", "member_portal", "member_selector", "membership_churn", "membership_credit_tracker", "membership_crm_tracker", "membership_dashboard", "membership_goal_tracker", "membership_insights_ai", "membership_loyalty_rewards", "membership_marketing_ai", "membership_ticketing_integration", "memberships_tool", "mentorship_center"],
    "🏟️ Events & Tournaments": ["event_control_panel", "event_creator_ai", "event_profit_analyzer", "event_types_config", "league_coordinator"],
}


with st.sidebar:
    st.header("🧭 Tool Categories")
    selected_category = st.selectbox("Category", list(CATEGORIES))
    selected_tool = st.selectbox("Tool", CATEGORIES[selected_category])

try:
    mod = importlib.import_module(selected_tool)
    if hasattr(mod, "run"):
        mod.run()
    else:
        st.warning("No run() function found in selected module.")
except Exception as e:
    st.error(f"Error loading module: {e}")