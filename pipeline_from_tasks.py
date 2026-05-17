from clearml.automation import PipelineController


def run_pipeline():
    pipe = PipelineController(
        name="Sydney_Housing_Basic_Pipeline",
        project="Sydney_Housing_Project",
        version="0.0.2",
        add_pipeline_tags=False,
    )

    pipe.set_default_execution_queue("tasks")

    pipe.add_step(
        name="stage_data_ingestion",
        base_task_project="Sydney_Housing_Project",
        base_task_name="V1_Data_Ingestion_and_EDA",
    )

    pipe.add_step(
        name="stage_feature_engineering",
        parents=["stage_data_ingestion"],
        base_task_project="Sydney_Housing_Project",
        base_task_name="V2_Feature_Engineering_Distance_Fixed",
    )

    pipe.add_step(
        name="stage_baseline_model",
        parents=["stage_feature_engineering"],
        base_task_project="Sydney_Housing_Project",
        base_task_name="V3_Baseline_RF_UltraClean",
    )

    pipe.add_step(
        name="stage_temporal_features",
        parents=["stage_baseline_model"],
        base_task_project="Sydney_Housing_Project",
        base_task_name="V4.1_Temporal_Features",
    )

    pipe.add_step(
        name="stage_pruned_rf_expert",
        parents=["stage_temporal_features"],
        base_task_project="Sydney_Housing_Project",
        base_task_name="V2.1_Pruned_RF_Expert",
    )

    pipe.start(queue="pipeline_controller")
    print("Pipeline submitted to ClearML. 🔥")


if __name__ == "__main__":
    run_pipeline()