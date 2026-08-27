from nena_component_tools.task_iterator import create_task_iterator

from component_pipeline import pipeline_function


def main():
    task_iterator = create_task_iterator()
    for task in task_iterator:
        output_dictionary = pipeline_function(task.input_dictionary)
        task.emit_event(output_dictionary=output_dictionary)


if __name__ == '__main__':
    main()
