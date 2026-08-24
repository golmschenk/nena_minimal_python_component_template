from nena_component_tools.task_iterator import create_task_iterator

from component_pipeline import pipeline_function


def main():
    task_iterator = create_task_iterator(upper_bound_run_time__seconds=60)
    for task in task_iterator:
        output_dictionary = pipeline_function(task.input_dictionary)
        task.emit_event(event_source='simple_python_component_pipeline', output_dictionary=output_dictionary)


if __name__ == '__main__':
    main()
