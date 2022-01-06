# Ensuring quality releases

This project consists of a several steps that are used to ensure quality release of a software.

### Terraform:
First step is to Create and Deploy Azure infrastructure. For creating and deploying insfrastructure, code in terraform folder is used. When executed, resource group, appservice, network, network security group, public IP and virtual machine are created.


### Teraform init output
![terraform_init_ci_cd_output](https://user-images.githubusercontent.com/53904394/148451110-b90f61fb-8d3e-41ae-9d52-c5db6cded16f.PNG)

### Terraform plan output
![terraform_plan_ci_cd_output](https://user-images.githubusercontent.com/53904394/148451906-f74bae95-cdeb-45bc-b974-396b164e6419.PNG)

### Terraform apply output
![terraform_apply_ci_cd_output](https://user-images.githubusercontent.com/53904394/148451927-c2528130-4e43-4e41-8e27-75f9bceda131.PNG)


## Azure DevOps CI/CD:

Three stages are defined: build, deploy and test, with several jobs that contain actions.

### Azure DevOps CI/CD pipeline execution

![successful_execution_of_the_pipeline](https://user-images.githubusercontent.com/53904394/148452161-a19fb6bf-68e2-4faa-a715-600a4f215682.PNG)

## Postman:

Postman is a tool used for Integration testing. Two test suites are executed, regression and data validation tests.

### Postman regression tests execution

![run_regression_tests_postman_ci_cd](https://user-images.githubusercontent.com/53904394/148452539-ac19373f-237c-4554-adbb-dbdc3021de90.PNG)

### Postman data validation tests execution

![run_data_validation_tests_postman_ci_cd](https://user-images.githubusercontent.com/53904394/148452590-75c42991-fcc4-4094-9800-396b62d6332c.PNG)

### Publish Postman test results

![publish_postman_test_results](https://user-images.githubusercontent.com/53904394/148452638-6024a339-ca70-4610-aa3e-b952b0e01983.PNG)

### Postman test summary page

![postman_test_summary_page](https://user-images.githubusercontent.com/53904394/148452679-8d893636-22b9-4220-af4f-d639450a17f1.PNG)

## Selenium:

Selenium is used for functional UI testing

### Selenium CI/CD execution

![selenium_ci_cd_job](https://user-images.githubusercontent.com/53904394/148452770-b20d5cb0-2841-4cb6-b99e-1cbe24bc8330.PNG)

## JMeter

JMeter is a tool used for Performance testing. Two test suites are executed, stress and endurance tests.

### Endurance tests CI/CD execution

![jmeter_endurance_test_ci_cd_execution](https://user-images.githubusercontent.com/53904394/148452993-67bb1d71-9dac-4981-a91b-e3842263e0b3.PNG)

### Endurance tests HTML report

![jmeter_endurance_test_html_report](https://user-images.githubusercontent.com/53904394/148453051-a7434dc9-9aeb-4e13-99c3-8f87ae757216.PNG)

### Stress tests CI/CD execution

![jmeter_stress_test_html_report](https://user-images.githubusercontent.com/53904394/148453071-60944105-d1cc-4aac-a0b0-2eaa1d6e2e72.PNG)

## Azure monitor

Azure monitor is used to configure alterts that trigger some action when specific condition is fulfilled.

### Created alert group

![alert_group](https://user-images.githubusercontent.com/53904394/148453286-1df6054b-9f27-4ce6-943b-2d4cb1610db3.PNG)

### Received email alert

![email_received_when_alert_is_triggered](https://user-images.githubusercontent.com/53904394/148453317-651dca57-8fa1-4e1f-a67a-c4861325ae36.PNG)

### Graph that represents number of requests that trigger alert

![graph_when_alert_is_triggered](https://user-images.githubusercontent.com/53904394/148453362-b3cb4513-e221-4d33-9c4a-c171a1095581.PNG)

## Configuring custom logging in Azure Monitor to ingest Selenium log file

### Selenium log file in Azure Monitor

![log_analytics_workspace_log_selenium](https://user-images.githubusercontent.com/53904394/148453591-e7a0c08e-6450-4067-a09a-b3d1b7db6a05.PNG)

### Selenium logging action in custom logging

![log_analytics_workspace_succesfull_login](https://user-images.githubusercontent.com/53904394/148453650-33bc8e1f-6286-4b24-b676-c2f2556e6093.PNG)

### Selenium add to cart in custom logging

![log_analytics_workspace_add_to_cart](https://user-images.githubusercontent.com/53904394/148453681-d5c8d954-9c5c-4be2-afe1-0b590a79e27b.PNG)

### Selenium remove from cart in custom logging

![log_analytics_workspace_remove_from_cart](https://user-images.githubusercontent.com/53904394/148453711-a4da454d-90f3-492e-9505-664fa72882a5.PNG)

