pipeline {
    agent {
        node {
            label "master"
        }
    }

    stages {
        stage('Ansible Playbook - Stop livability app') {
            steps {
                script {
                    echo "Ansible Playbook - Start livability app"
                    sh "ansible-playbook -i scripts/ansible-playbooks/inventory.yml scripts/ansible-playbooks/stop_livability.yml"
                }
            }
            post {
                failure {
                    error("Ansible Playbook - Stop livability app steps failed, please handle it!")
                }
                aborted {
                    error("Ansible Playbook - Stop livability app steps failed. Stopping operation!")
                }
            }
        }
    }
}