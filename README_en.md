# Todoapp

<img
  src="img/app.png"
  alt="Todoapp"
  title="Todoapp"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

This repository contains a Kubernetes demo app comprising multiple microservices.
This app showcases various Istio features but can also be used in other demo scenarios without Istio.

The app includes the following microservices:
- `todoapp`: Primary microservice for populating a page with content.
- `recommend`: Microservice providing recommendations.
- `redis`: Microservice for storing submitted information.

`todoapp` comes in two versions:
- `v1`: Makes no calls to `recommend`.
- `v2`: Makes calls to `recommend` and outputs the result.

The app looks like this:

<img
  src="img/diagram.png"
  alt="Todoapp Diagram"
  title="Todoapp Diagram"
  style="display: inline-block; margin: 0 auto; max-width: 400px">

## Installation

To install the app, run this command:

```
kubectl apply -f kube/todoapp.yaml
```
 
If Istio is deployed in the cluster, you can publish your app by creating a gateway and virtual service:

 ```
 kubectl apply -f kube/todoapp-gateway.yaml
 ```

The app will be accessible via the IP address of the Istio ingress gateway.

 ## Tutorial

 For a step-by-step tutorial using this example, see the relevant Yandex Cloud documentation.
