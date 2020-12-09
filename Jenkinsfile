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
            	sh '''  python Pruebas/prueba1.py
                        python Pruebas/prueba2.py
                        python Pruebas/prueba3.py
                        python Pruebas/prueba4.py
                        python Pruebas/prueba5.py
                        python Pruebas/prueba6.py
                        python Pruebas/prueba7.py
                        python Pruebas/prueba8.py
                        python Pruebas/prueba9.py
                        python Pruebas/prueba10.py
                        python Pruebas/prueba11.py
                        python Pruebas/prueba12.py
                        python Pruebas/prueba13.py
                        python Pruebas/prueba14.py
                        python Pruebas/prueba15.py
                        python Pruebas/prueba16.py
                        python Pruebas/prueba17.py
                        python Pruebas/prueba18.py
                        python Pruebas/prueba19.py
                        python Pruebas/prueba20.py
                        python Pruebas/prueba21.py
                        python Pruebas/prueba22.py
                        python Pruebas/prueba23.py
                        python Pruebas/prueba24.py
                        python Pruebas/prueba25.py
                        python Pruebas/prueba26.py
                        python Pruebas/prueba27.py
                        python Pruebas/prueba28.py
                        python Pruebas/prueba29.py
                        python Pruebas/prueba30.py
                        python Pruebas/prueba31.py
                        python Pruebas/prueba32.py
                        python Pruebas/prueba33.py
                        python Pruebas/prueba35.py
                        python Pruebas/prueba36.py
                        python Pruebas/prueba37.py
                        python Pruebas/prueba38.py
                        python Pruebas/prueba39.py
                        python Pruebas/prueba40.py
                        python Pruebas/prueba41.py
                        python Pruebas/prueba42.py
            		
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
