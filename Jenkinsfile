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
				sh '''
					bash -c "virtualenv entorno_virtual && source entorno_virtual/bin/activate"
				'''

            }
        }
	stage('Requerimientos') {
            steps {
            	sh '''
            		bash -c "source ${WORKSPACE}/entorno_virtual/bin/activate && ${WORKSPACE}/entorno_virtual/bin/python ${WORKSPACE}/entorno_virtual/bin/pip install -r requirements.txt"
			
			
                '''
            }
        }   
        stage('TestApp') {
            steps {
            	sh '''  bash -c " source ${WORKSPACE}/Pruebas prueba1.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba2.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba3.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba4.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba5.py && 
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba6.py && 
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba7.py && 
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba8.py && 
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba9.py && 
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba10.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba11.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba12.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba13.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba14.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba15.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba16.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba17.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba18.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba19.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba20.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba21.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba22.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba23.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba24.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba25.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba26.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba27.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba28.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba29.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba30.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba31.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba32.py &&
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba33.py && 
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba35.py && 
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba36.py && 
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba37.py && 
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba38.py && 
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba39.py && 
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba40.py && 
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba41.py && 
                        ${WORKSPACE}/entorno_virtual/bin/python Pruebas/prueba42.py "
            		
                '''
            }
        }  
        stage('RunPagina') {
            steps {
            	sh '''
            		bash -c "source entorno_virtual/bin/activate ; ${WORKSPACE}/entorno_virtual/bin/python ${WORKSPACE}/manage.py runserver &"
                '''
            }
        } 
        stage('ConstruirDocker') {
            steps {
            	sh '''
            		docker build -t prueba1 .
                '''
            }
        } 
    stage('SubirImagenDocker') {
            steps {
            	sh '''
            		docker tag prueba1:latest daniifreen/prueba1:latest
			        docker push daniifreen/prueba1:latest
			        docker rmi prueba1:latest
                '''
            }
        } 
  }
}
