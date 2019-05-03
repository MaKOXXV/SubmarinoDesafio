#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building...'
                git 'https://github.com/MaKOXXV/SubmarinoDesafio'
            }
        }
        stage ("Test"){
            steps{
                bat '''
                pip install python-jenkins
                python -m pip install --upgrade pip
                pip install virtualenv
                virtualenv env
                env//Scripts//activate
                '''
                bat '''
                cd submarinoChrome
                python -m Pyautomators -f json -o .//submarinoChrome.json
                '''
              
            }
        }
    }
}
