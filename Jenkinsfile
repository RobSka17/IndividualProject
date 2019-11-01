pipeline{
        agent any
        stages{ 
		    stage('---Build_Image---'){
                        steps{
                            echo "Building image..."
                            sh "sudo docker build -t cyraz-wor ."
                        }
                }
                stage('---Clean---'){
                        steps{
                              sh label: '', script: '''if [ "$(sudo docker ps -qa -f name=cyraz-wor)" ]; then
       				 		# cleanup
        					sudo docker rm -f cyraz-wor
				fi'''
                        }
                }
                stage('---Run---'){
                    steps{
                    # run your container
				sudo docker run -d --name cyraz-wor -p 5000:5000 cyraz-wor
                    }
                }
        }
}
