pipeline
{
        agent any
        stages
	{ 
		    stage('Build Image')
		{
                        steps
			{
                            echo "Building image..."
                            sh "docker build -t cyraz-wor ."
                        }
                }
                stage('Clean-Up')
		{
                        steps
			{
				cleanWs()
                              sh label: '', script: '''if [ "$(docker ps -qa -f name=cyraz-wor)" ]; then
        					docker rm -f cyraz-wor
				fi'''
                        }
                }
                stage('Run')
		{
                    steps
			{
				sh "docker run -d --name cyraz-wor -p 5000:5000 cyraz-wor"
                    	}
                }
        }
}
