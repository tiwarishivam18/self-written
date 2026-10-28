Important commands:

Deployment:
kubectl create deployment nginx --image=nginx --replicas=3  
kubectl scale deployment nginx --replicas=5

Pods:
kubectl get pods -o wide
kubectl run nginx --image=nginx
kubectl exec -it nginx-storage -c nginx -- bash


Networking:
kubectl port-forward pod/<pod-name> <local-port>:<pod-port>



