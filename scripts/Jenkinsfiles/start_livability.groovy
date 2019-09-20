pipeline {
    agent {
        node {
            label "master"
        }
    }

    environment {
        ANSIBLE_STAGE_NAME = "Start Livability App"
        ANSIBLE_PLAYBOOK_CMD = "/Library/Frameworks/Python.framework/Versions/3.7/bin/ansible-playbook"
        ANSIBLE_VAULT_PASSWORD_FILE = "/Users/Shared/Jenkins/.vp"
        PLAYBOOK_DIR = "scripts/ansible-playbooks"
    }

    stages {
        stage("Ansible Playbook - ${ANSIBLE_STAGE_NAME}") {
            steps {
                script {
                    echo "Ansible Playbook - ${ANSIBLE_STAGE_NAME}"
                    sh "${ANSIBLE_PLAYBOOK_CMD} -i ${PLAYBOOK_DIR}/inventory.yml " +
                            "${PLAYBOOK_DIR}/start_livability.yml " +
                            "--vault-password=${ANSIBLE_VAULT_PASSWORD_FILE}"
                }
            }
            post {
                success {
                    slackSend(channel: '#automation_notifications', message: "Ansible Playbook - ${ANSIBLE_STAGE_NAME} - Success")
                }
                failure {
                    error("Ansible Playbook - ${ANSIBLE_STAGE_NAME} steps failed, please handle it!")
                }
                aborted {
                    error("Ansible Playbook - ${ANSIBLE_STAGE_NAME} steps failed. Stopping operation!")
                }
            }
        }
    }
}
