import dash_mantine_components as dmc
from dash import html

# Available models for the dropdown
AUDIO_MODELS = [
    {"value": "model1", "label": "Model 1"},
    {"value": "model2", "label": "Model 2"},
    {"value": "model3", "label": "Model 3"},
]

layout = dmc.Grid(
    children=[
        # Left Column - Audio Generation
        dmc.GridCol(
            span=6,
            children=[
                dmc.Paper(
                    p="md",
                    shadow="xs",
                    children=[
                        dmc.Title("Audio Generation", order=2, mb="md"),
                        
                        # Model Selection Dropdown
                        dmc.Select(
                            label="Select Model",
                            placeholder="Choose a model",
                            data=AUDIO_MODELS,
                            id="model-select",
                            mb="md",
                        ),
                        
                        # Prompt Text Area
                        dmc.Textarea(
                            label="Audio Description",
                            placeholder="Describe the audio you want to generate...",
                            minRows=3,
                            id="audio-prompt",
                            mb="md",
                        ),
                        
                        # Advanced Configurations (Collapsible)
                        dmc.Accordion(
                            children=[
                                dmc.AccordionItem(
                                    children=[
                                        # Placeholder for advanced configurations
                                        dmc.Text("Advanced settings will be added here"),
                                    ],
                                    value="advanced-configurations",
                                ),
                            ],
                            mb="md",
                        ),
                        
                        # Generate Button
                        dmc.Button(
                            "Generate Audio",
                            id="generate-btn",
                            fullWidth=True,
                            color="blue",
                        ),
                    ]
                )
            ]
        ),
        
        # Right Column - My Generations
        dmc.GridCol(
            span=6,
            children=[
                dmc.Paper(
                    p="md",
                    shadow="xs",
                    children=[
                        dmc.Title("My Generations", order=2),
                        # Placeholder for generated audio list
                        dmc.Text("Your generated audio files will appear here"),
                    ]
                )
            ]
        ),
    ],
    gutter="xl",
)
