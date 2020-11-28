// comment
pipeline {
 agent any
 stages {
        stage('Checkout-git'){
               steps{
		git poll: true, url: 'git@github.com:andresgh10/Web.git'
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
        //stage('TestApp') {
          //  steps {
            	//sh '''                      aqui van las pruebas unitarias de la pagina web
            		
                //'''
            //}
        //}  
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
            		docker build -t web_web:latest .
                '''
            }
        } 
    stage('SubirImagenDocker') {
            steps {
            	sh '''
            		docker tag web_web:latest daniifreen/web_web:latest
			        docker push daniifreen/web_web:latest
			        docker rmi web_web:latest
                '''
            }
        } 
  }
}
