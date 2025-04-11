node {

    stage('Checkout') {
        checkout scm
    }

    def customImage 
    stage('Build and Test') {
        customImage = docker.build("ryadhamdini/calc-py:${env.BUILD_ID}")

        customImage.inside {
            sh 'pytest'
        }
    }

    stage('Push Image') {
        docker.withRegistry('https://index.docker.io/v1/', 'bed905e0-659f-409e-afbb-c9efbc78ac20'){
            customImage.push()
        }
    }
}