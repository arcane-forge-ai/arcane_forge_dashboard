import dash_mantine_components as dmc

layout = dmc.Timeline(
    active=1,
    bulletSize=15,
    lineWidth=2,
    children=[
        dmc.TimelineItem(
            title="Needs Review",
            children=[
                dmc.Text(
                    [
                        "Your SCA ",
                        dmc.Anchor("application", href="#", size="sm"),
                        "has been reviewed",
                    ],
                    c="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="First Submission",
            children=[
                dmc.Text(
                    [
                        "Your SCA application has been submitted.",
                    ],
                    c="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(title="1st Level Internal Appealing", ),
        dmc.TimelineItem(
            title="2nd Level Internal Appealing",
            lineVariant="dashed",
        ),
        dmc.TimelineItem(
            title="2nd Level Internal Appealing",
            lineVariant="dashed",
        ),
        dmc.TimelineItem(
            title="External Appealing",
            lineVariant="dashed",
        ),
        dmc.TimelineItem(
            title="Grievance",
            lineVariant="dashed",
        ),
        dmc.TimelineItem(
            title="Handoff",
            lineVariant="dashed",
        ),
    ],
)
