# Apple Quality Classification in Azure

Autores:

    Eduardo Miguel Riederer
    Samuel Reyes Sanz

# Descripción

Este proyecto se centra en la clasificación de la calidad de las manzanas utilizando técnicas de Machine Learning (ML) en Azure. Implementamos un pipeline completo desde la ingestión de datos hasta el entrenamiento y la inferencia del modelo en el entorno de Azure ML y Synapse.
Dataset

El dataset utilizado para entrenar el modelo de clasificación de calidad de manzanas puede encontrarse en Kaggle: https://www.kaggle.com/datasets/nelgiriyewithana/apple-quality/data

El análisis exploratorio de datos (EDA) relevante se encuentra aquí: https://www.kaggle.com/code/bryamblasrimac/applequality-eda-classification-multiplemodels
# 1. Integración con Azure Synapse

El primer paso es integrar Azure ML con Synapse para el manejo eficiente de los datos y el entrenamiento de modelos escalables. Usamos la autenticación de Azure y conectamos con el workspace de Synapse utilizando el MLClient para configurar nuestro ambiente de ML.
# 2. Preparación de Datos

Los datos son almacenados y gestionados a través de Azure Data Lake y accesibles mediante Azure Synapse. Utilizamos Azure ML para registrar el datastore, listar archivos en el almacenamiento y cargar los datos necesarios para el entrenamiento.
# 3. Entrenamiento del Modelo

El script train_model.ipynb contiene el código necesario para preparar los datos, entrenar el modelo de clasificación usando un MLP (Multi-Layer Perceptron), hacer log de las métricas y registrar el modelo dentro del entorno de Azure ML. Se emplea MLflow para el seguimiento de experimentos y la gestión del ciclo de vida del modelo.
# 4. Inference

Demostramos cómo el modelo realiza inferencias sobre nuevos datos. La inferencia se lleva a cabo a través de un endpoint creado en Azure ML sobre el modelo previamente entrenado, facilitando la clasificación de nuevas instancias de manzanas en tiempo real.

Model Inference
# Cómo Usar

Para replicar este proyecto:

    Clone el repositorio a su entorno local o de Azure.
    Asegúrese de tener configurado un entorno Azure ML y acceso a Azure Synapse.
    Siga los pasos en train_model.ipynb para el entrenamiento del modelo y inference.ipynb (deberías crear este basado en la estructura de tu proyecto) para realizar inferencias.

Este proyecto es un ejemplo práctico de cómo integrar y utilizar las capacidades de Azure para el desarrollo de soluciones de ML end-to-end.
