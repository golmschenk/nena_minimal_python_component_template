FROM python:3.14-slim

WORKDIR /workspace
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
COPY nena_component_tools ./nena_component_tools
RUN pip install --no-cache-dir ./nena_component_tools
RUN rm -rf nena_component_tools

COPY nena_python_container_template/component_pipeline.py .
COPY nena_python_container_template/container_loop.py .
CMD ["python", "./container_loop.py"]
