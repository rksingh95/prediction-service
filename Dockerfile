FROM continuumio/miniconda3:latest

WORKDIR /app

# Install myapp requirements
COPY environment.yml /app/environment.yml
RUN conda config --add channels conda-forge \
    && conda env create -n myapp -f environment.yml \
    && rm -rf /opt/conda/pkgs/*

# Copy all files after to avoid rebuild the conda env each time
COPY . /app/


# activate the myapp environment
ENV PATH /opt/conda/envs/myapp/bin:$PATH

# Launch the API
CMD ["python", "index.py"]