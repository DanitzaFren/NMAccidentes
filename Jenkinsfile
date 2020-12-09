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
        stage('RunPagina') {
            steps {
            	sh '''
            		bash -c "source entorno_virtual/bin/activate ; ${WORKSPACE}/entorno_virtual/bin/python ${WORKSPACE}/manage.py runserver &"
                '''
            }
        } 
        stage('TestApp') {
            steps {
                echo "-=- ejecutando pruebas unitarias Selenium en Chrome -=-"
                sh "python3 Pruebas/prueba1.py"
                sh "python3 Pruebas/prueba2.py"
                sh "python3 Pruebas/prueba4.py"
                sh "python3 Pruebas/prueba5.py"
                sh "python3 Pruebas/prueba6.py"
                sh "python3 Pruebas/prueba7.py"
                sh "python3 Pruebas/prueba8.py"
                sh "python3 Pruebas/prueba9.py"
                sh "python3 Pruebas/prueba10.py"
                sh "python3 Pruebas/prueba11.py"
                sh "python3 Pruebas/prueba12.py"
                sh "python3 Pruebas/prueba13.py"
                sh "python3 Pruebas/prueba14.py"
                sh "python3 Pruebas/prueba15.py"
                sh "python3 Pruebas/prueba16.py"
                sh "python3 Pruebas/prueba20.py"
                sh "python3 Pruebas/prueba21.py"
                sh "python3 Pruebas/prueba22.py"
                sh "python3 Pruebas/prueba23.py"
                sh "python3 Pruebas/prueba24.py"
                sh "python3 Pruebas/prueba25.py"
                sh "python3 Pruebas/prueba26.py"
                sh "python3 Pruebas/prueba27.py"
                sh "python3 Pruebas/prueba28.py"
                sh "python3 Pruebas/prueba29.py"
                sh "python3 Pruebas/prueba30.py"
                sh "python3 Pruebas/prueba31.py"
                sh "python3 Pruebas/prueba32.py"
                sh "python3 Pruebas/prueba33.py"
                sh "python3 Pruebas/prueba34.py"
                sh "python3 Pruebas/prueba35.py"
                sh "python3 Pruebas/prueba36.py"
                sh "python3 Pruebas/prueba37.py"
                sh "python3 Pruebas/prueba38.py"
                sh "python3 Pruebas/prueba39.py"
                sh "python3 Pruebas/prueba40.py"
                sh "python3 Pruebas/prueba41.py"
                sh "python3 Pruebas/prueba42.py"

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
