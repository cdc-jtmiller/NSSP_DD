from shiny import App, ui, render, reactive
import datetime

app_ui = ui.page_fluid(
    ui.h2("NSSP BioSense Platform – Data Deletion Request Form (Proof of Concept)"),
    ui.hr(),

    ui.panel_title("Requestor Information"),
    ui.input_text("name", "Name"),
    ui.input_text("role", "Role (e.g., Epidemiologist, Jurisdiction Administrator)"),
    ui.input_text("email", "Email"),
    ui.input_text("site", "Site"),
    ui.input_date("submission_date", "Date of Submission", value=datetime.date.today()),

    ui.hr(),
    ui.panel_title("Reason for Deletion"),
    ui.input_text_area("reason", "Please provide a detailed description explaining why this data needs to be deleted.", rows=3),

    ui.hr(),
    ui.panel_title("Description of Request"),
    ui.input_text_area(
        "description",
        "Describe the specific data or records to be deleted. Include Start/End Dates (and type), Facility Name(s)/ID(s), File names, etc.",
        rows=4
    ),

    ui.hr(),
    ui.panel_title("Select Affected Data"),

    ui.h4("Raw Data Files"),
    ui.input_checkbox_group(
        "raw_data_files",
        "Select all that apply:",
        {
            "staging_hl7": "Staging Raw HL7 Data Files",
            "production_hl7": "Production Raw HL7 Data Files",
            "staging_csv": "Staging Raw CSV Data Files",
            "production_csv": "Production Raw CSV Data Files",
            "staging_mor": "Staging Raw MOR Data Files",
            "production_mor": "Production Raw MOR Data Files"
        }
    ),

    ui.h4("SQL Tables"),
    ui.input_checkbox_group(
        "sql_tables",
        "Select all that apply:",
        {
            "essence_staging": "ESSENCE Application (Staging)",
            "essence_production": "ESSENCE Application (Production)",
            "archive_raw_staging": "Archive – Raw (Staging)",
            "archive_raw_production": "Archive – Raw (Production)",
            "archive_processed_staging": "Archive – Processed (Staging)",
            "archive_processed_production": "Archive – Processed (Production)",
            "archive_exceptions_staging": "Archive – Exceptions (Staging)",
            "archive_exceptions_production": "Archive – Exceptions (Production)",
            "mortality_raw_staging": "Mortality – Raw (Staging)",
            "mortality_raw_production": "Mortality – Raw (Production)",
            "mortality_processed_staging": "Mortality – Processed (Staging)",
            "mortality_processed_production": "Mortality – Processed (Production)",
            "mortality_exceptions_staging": "Mortality – Exceptions (Staging)",
            "mortality_exceptions_production": "Mortality – Exceptions (Production)"
        }
    ),
    ui.input_text_area("other_sql_tables", "Other SQL tables (please specify):", rows=2),

    ui.hr(),
    ui.panel_title("Data Identification SQL Query"),
    ui.input_text_area("sql_query", "Please indicate the specific SQL queries that can be used to identify the data to be deleted.", rows=4),

    ui.hr(),
    ui.input_action_button("submit", "Submit Request", class_="btn-primary"),

    ui.output_ui("confirmation")

    ui.hr(),
    ui.panel_title("Total Records Affected"),
    ui.input_checkbox_group(
      "records_affected_type",
      "Select the type(s) of records affected:",
      {
        "hl7": "HL7 messages",
        "visits": "Visits (line-level data)",
        "both": "Both"
      }
    ),
    ui.input_text("records_affected_count", "Enter the total number of records affected:"),
    )

def server(input, output, session):
    @reactive.event(input.submit)
    def _():
        # For demonstration, just show a confirmation with the entered data
        output.confirmation.set_ui(
            ui.panel_well(
                ui.h4("Submission Received"),
                ui.p("Thank you! Here is a summary of your request:"),
                ui.tags.ul(
                    ui.tags.li(f"Name: {input.name()}"),
                    ui.tags.li(f"Role: {input.role()}"),
                    ui.tags.li(f"Email: {input.email()}"),
                    ui.tags.li(f"Site: {input.site()}"),
                    ui.tags.li(f"Date of Submission: {input.submission_date()}"),
                    ui.tags.li(f"Reason for Deletion: {input.reason()}"),
                    ui.tags.li(f"Description: {input.description()}"),
                    ui.tags.li(f"Raw Data Files: {', '.join(input.raw_data_files())}"),
                    ui.tags.li(f"SQL Tables: {', '.join(input.sql_tables())}"),
                    ui.tags.li(f"Other SQL Tables: {input.other_sql_tables()}"),
                    ui.tags.li(f"SQL Query: {input.sql_query()}"),
                )
            )
        )

app = App(app_ui, server)
