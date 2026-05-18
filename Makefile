.PHONY: run-dev run-test run-prod

# Inicia la aplicación en modo desarrollo local con autorecarga activa
run-dev:
	export FLASK_ENV=development && python app.py

# Prepara las variables necesarias para ejecutar las suites de pruebas de forma aislada
run-test:
	export FLASK_ENV=testing && pytest

# Configura las optimizaciones de seguridad y rendimiento para despliegue final
run-prod:
	export FLASK_ENV=production && gunicorn -w 4 "app:create_app()"