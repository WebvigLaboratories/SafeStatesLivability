pipeline {
    agent {
        node {
            label "master"
        }
    }

    stages {
        stage('Ansible Playbook - Start livability app') {
            steps {
                script {
                    echo "Ansible Playbook - Start livability app"
                    sh "ansible-playbook -i scripts/ansible-playbooks/inventory.yml scripts/ansible-playbooks/start_livability.yml"
                }
            }
            post {
                failure {
                    error("Ansible Playbook - Start livability app steps failed, please handle it!")
                }
                aborted {
                    error("Ansible Playbook - Start livability app steps failed. Stopping operation!")
                }
            }
        }
    }
}