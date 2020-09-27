class Grandparent(object):
    def my_method(self):
        print "Grandparent"

class Parent(Grandparent):
    def my_method(self):
        print "Parent"

class Child(Parent):
    def my_method(self):
        print "Hello Grandparent"
        super(Child, self).my_method()



a = Child()
print(a.my_method())










REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
mysite_web                 latest              f80d103a0d8a        2 minutes ago       1.06GB
<none>                     <none>              cfe072a46a63        19 minutes ago      1.06GB
d_h_g_web                  latest              672c68097612        38 minutes ago      932MB
web                        latest              625dc31e7296        49 minutes ago      334MB
<none>                     <none>              f422180b057c        59 minutes ago      330MB
django_application_image   latest              6690df90240d        About an hour ago   330MB
<none>                     <none>              e8a0ae06751f        About an hour ago   330MB
<none>                     <none>              b0c70d11a86a        21 hours ago        1.05GB
python                     3.8-alpine          ff6233d0ceb9        2 days ago          42.9MB
python                     3                   bbf31371d67d        2 days ago          882MB
postgres                   latest              817f2d3d51ec        2 days ago          314MB
hello-world                latest              bf756fb1ae65        8 months ago        13.3kB
dnyanesh@dm:~/projects/mysite$









 docker rmi f422180b057c 
 docker rmi e8a0ae06751f
 docker rmi b0c70d11a86a
 docker rmi cfe072a46a63
