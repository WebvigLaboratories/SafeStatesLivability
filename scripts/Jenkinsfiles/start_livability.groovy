pipeline {
    agent {
        node {
            label "master"
        }
    }

    environment {
        ANSIBLE_PLAYBOOK_CMD = "/Library/Frameworks/Python.framework/Versions/3.7/bin/ansible-playbook"
        ANSIBLE_VAULT_PASSWORD_FILE = "/User/Shared/Jenkins/.vp"
        PLAYBOOK_DIR = "scripts/ansible-playbooks"
    }

    stages {
        stage('Ansible Playbook - Start livability app') {
            steps {
                script {
                    echo "Ansible Playbook - Start livability app"
                    sh "${ANSIBLE_PLAYBOOK_CMD} -i ${PLAYBOOK_DIR}/inventory.yml " +
                            "${PLAYBOOK_DIR}/start_livability.yml " +
                            "--vault-password=${ANSIBLE_VAULT_PASSWORD_FILE}"
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