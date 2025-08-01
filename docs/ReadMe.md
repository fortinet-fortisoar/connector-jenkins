
<h2>About the connector</h2>

<p>Jenkins is an open-source automation server widely used to implement Continuous Integration (CI) and Continuous Delivery (CD) pipelines. It helps automate the parts of software development related to building, testing, and deploying, facilitating faster and more reliable software delivery.</p>

<p>This document provides information about the Jenkins connector, which facilitates automated interactions, with a Jenkins server using FortiSOAR&trade; playbooks. Add the Jenkins connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Jenkins.</p>

<h3>Version information</h3>

<p>Connector Version: 1.0.0</p>

<p>FortiSOAR&trade; Version Tested on: 7.4.1-3167</p>

<p>Jenkins Version Tested on: </p>

<p>Authored By: Fortinet</p>

<p>Certified: No</p>

<h2>Installing the connector</h2>

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>

<pre>yum install cyops-connector-jenkins</pre>

<h2>Prerequisites to configuring the connector</h2>

<ul>
<li>You must have the credentials of Jenkins server to which you will connect and perform automated operations.</li>
<li>The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Jenkins server.</li>
</ul>

<h2>Minimum Permissions Required</h2>

<ul>
<li>Not applicable</li>
</ul>

<h2>Configuring the connector</h2>

<p>For the procedure to configure a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector">here</a></p>

<h3>Configuration parameters</h3>

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Jenkins</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Provide the host URL of the jenkins server to connect and perform automated operations.</td></tr>
<tr><td>Username</td><td>Username of the jenkins server to which you will connect and perform automated operations.</td></tr>
<tr><td>API Token</td><td>Specify the API token of the jenkins server to which you will connect and perform automated operations.</td></tr>
<tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified. <br/>By default, this option is selected, i.e., set to <code>true</code>.</td></tr>
</tbody></table>

<h2>Actions supported by the connector</h2>

<p>You can use the following automated operations in playbooks and also use the annotations to access operations:</p>

<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get List Jobs</td><td>Retrieves a list of all available jobs from the Jenkins server.</td><td>get_list_jobs <br/>Investigation</td></tr>
<tr><td>Trigger Job</td><td>Triggers a Jenkins job with specified parameters.</td><td>trigger_job <br/>Investigation</td></tr>
<tr><td>Get Job Status</td><td>Retrieves the current status and details of the specified Jenkins job.</td><td>get_job_status <br/>Investigation</td></tr>
<tr><td>Resume Jenkins Job with Input</td><td>Submits input to a paused Jenkins pipeline job that is waiting at a user input to resume execution.</td><td>resume_jenkins_job_with_input <br/>Investigation</td></tr>
<tr><td>Execute an API Request</td><td>Sends an API request to any API endpoint based on specified HTTP method, endpoint, and other input parameters that you have specified, enabling flexible API interactions tailored to user needs.</td><td>generic_rest_api_call <br/>Investigation</td></tr>
</tbody></table>

<h3>operation: Get List Jobs</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job Path</td><td>(Optional) Specify the name or full path of the Jenkins job to retrieve the list of jobs. For jobs inside folders, include the full folder hierarchy using repeated /job/ segments.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "_class": "",
    "assignedLabels": [
        {}
    ],
    "mode": "",
    "nodeDescription": "",
    "nodeName": "",
    "numExecutors": "",
    "description": "",
    "jobs": [
        {
            "_class": "",
            "name": "",
            "url": "",
            "color": ""
        }
    ],
    "overallLoad": {},
    "primaryView": {
        "_class": "",
        "name": "",
        "url": ""
    },
    "quietingDown": "",
    "slaveAgentPort": "",
    "unlabeledLoad": {
        "_class": ""
    },
    "useCrumbs": "",
    "useSecurity": "",
    "views": [
        {
            "_class": "",
            "name": "",
            "url": ""
        }
    ]
}</pre>

<h3>operation: Trigger Job</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job Path</td><td>Specify the name or full path of the Jenkins job to be triggered. For jobs inside folders, include the full folder hierarchy using repeated /job/ segments</td></tr>
<tr><td>Build Parameters</td><td>(Optional) Specify the parameters in JSON format as key-value pairs to be passed to the job</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "job_name": "",
    "build_no": "",
    "job_build_url": ""
}</pre>

<h3>operation: Get Job Status</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job Path</td><td>Specify the name or full path of the Jenkins job Jenkins job to retrieve its status and detailed information. For jobs inside folders, include the full folder hierarchy using repeated /job/ segments</td></tr>
<tr><td>Build Number</td><td>Specify the build number of the Jenkins job to retrieve its status and detailed information.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "_class": "",
    "actions": [
        {
            "_class": "",
            "parameters": [
                {
                    "_class": "",
                    "name": "",
                    "value": ""
                }
            ]
        },
        {
            "_class": "",
            "causes": [
                {
                    "_class": "",
                    "shortDescription": "",
                    "userId": "",
                    "userName": ""
                }
            ]
        }
    ],
    "artifacts": [],
    "building": "",
    "description": "",
    "displayName": "",
    "duration": "",
    "estimatedDuration": "",
    "executor": "",
    "fullDisplayName": "",
    "id": "",
    "keepLog": "",
    "number": "",
    "queueId": "",
    "result": "",
    "timestamp": "",
    "url": "",
    "builtOn": "",
    "changeSet": {
        "_class": "",
        "items": [],
        "kind": ""
    }
}</pre>

<h3>operation: Resume Jenkins Job with Input</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job Path</td><td>Specify the name or full path of the Jenkins job to resume. For jobs inside folders, include the full folder hierarchy using repeated /job/ segments</td></tr>
<tr><td>Build Number</td><td>Specify the build number of the Jenkins job to resume execution with user-provided input.</td></tr>
<tr><td>Input ID</td><td>Specify the unique identifier for a specific input step or approval request within a Jenkins build.</td></tr>
<tr><td>Input Parameters</td><td>Specify the parameters as key-value pairs in JSON format to be passed to the job and resume execution.
For example: [{"name":"param1","value":"valueOfParam1"},{"name":"param2","value":"valueOfParam2"}]</td></tr>
<tr><td>Job Status</td><td>Specify the parameters as key-value pairs in JSON format to be passed to the job and resume execution.
For example: [{"name":"param1","value":"valueOfParam1"},{"name":"param2","value":"valueOfParam2"}]</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "status": "",
    "response": ""
}</pre>

<h3>operation: Execute an API Request</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Endpoint URL</td><td>Specify the target API URL path for the request. For example, if the website is https://example.com and URL path is https://example.com/api/v2/incidents/search, the endpoint would be /api/v2/incidents/search.</td></tr>
<tr><td>Method</td><td>Select an HTTP action for the request. You can select from the following options: GET, DELETE, PATCH, POST, PUT.</td></tr>
<tr><td>Query Parameters</td><td>(Optional) Specify any optional parameters to add to the URL and refine the request.</td></tr>
<tr><td>Payload</td><td>(Optional) Specify data, as JSON, to be sent as the request payload (typically for POST or PUT requests).</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h2>Included playbooks</h2>

<p>The <code>Sample - Jenkins - 1.0.0</code> playbook collection comes bundled with the Jenkins connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the <strong>Automation</strong> &gt; <strong>Playbooks</strong> section in FortiSOAR&trade; after importing the Jenkins connector.</p>

<ul>
<li>Execute an API Request</li>
<li>Get Job Status</li>
<li>Get List Jobs</li>
<li>Resume Jenkins Job with Input</li>
<li>Trigger Job</li>
</ul>

<p><strong>Note</strong>: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.</p>

<h2>Data Ingestion Support</h2>

<p>Use the Data Ingestion Wizard to easily ingest data into FortiSOAR&trade; by pulling events/alerts/incidents, based on the requirement.</p>

<p><strong>TODO:</strong> provide the list of steps to configure the ingestion with the screen shots and limitations if any in this section.</p>
