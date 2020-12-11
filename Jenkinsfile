// comment
pipeline {
 agent any
 stages {
        stage('Checkout-git'){
               steps{
		git poll: true, url: 'git@github.com:daniifreen/NMAccidentes.git'
               }
        }
        
        stage('crearEntornoVirtual') {
            steps {
                echo "-=- Creación del entorno virtual. -=-"
				sh '''
					bash -c "virtualenv entorno_virtual && source entorno_virtual/bin/activate"
				'''

            }
        }
	stage('Requerimientos') {
            steps {
                echo "-=- Instalación de los requerimientos. -=-"
            	sh '''
            		bash -c "source ${WORKSPACE}/entorno_virtual/bin/activate && ${WORKSPACE}/entorno_virtual/bin/python ${WORKSPACE}/entorno_virtual/bin/pip install -r requirements.txt"
			
			
                '''
            }
        }   
        stage('EjecutarPágina') {
            steps {
                echo "-=- Despliegue local de la página Web. -=-"
            	sh '''
            		bash -c "source entorno_virtual/bin/activate ; ${WORKSPACE}/entorno_virtual/bin/python ${WORKSPACE}/manage.py runserver &"
                '''
            }
        } 
        stage('PruebasUnitarias') {
            steps {
                echo "-=- Ejecución de pruebas unitarias Selenium en Chrome -=-"
                sh "python3 Pruebas/prueba1.py && python3 Pruebas/prueba2.py && python3 Pruebas/prueba3.py && python3 Pruebas/Prueba6.py && python3 Pruebas/Prueba7.py"                  //
            }
        }  
        stage('ConstruirDocker') {
            steps {
                echo "-=- Construcción de la imagen Docker. -=-"
            	sh '''
            		docker build -t prueba1 .
                '''
            }
        } 
    stage('SubirImagenDocker') {
            steps {
                echo "-=- Imagen de Docker en el repositorio. -=-"
            	sh '''
            		docker tag prueba1:latest daniifreen/prueba1:latest
			        docker push daniifreen/prueba1:latest
			        docker rmi prueba1:latest
                '''
            }
        } 
  }
}
