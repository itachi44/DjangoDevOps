FROM python:3.9  

# Set working directory and app folder
ENV APP_FOLDER=/home/app/webapp
RUN mkdir -p $APP_FOLDER  
WORKDIR $APP_FOLDER  

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# Update pip version
RUN pip install --upgrade pip  

# Copy requirements file
COPY requirements.txt .

# Create a virtual environment
RUN python -m venv env

# Activate virtual environment
RUN . env/bin/activate

# Upgrade pip and Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy application code
COPY . $APP_FOLDER

#  Copy the entrypoint
COPY entrypoint.sh .

# make entrypoint.sh executable
RUN chmod +x entrypoint.sh

# Expose port
EXPOSE 8000

# set entrypoint
ENTRYPOINT ["./entrypoint.sh"]

