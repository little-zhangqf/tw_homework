FROM ubuntu:latest
ADD jdk-8u151-linux-x64.tar.gz /root
RUN mkdir -p /opt/java
RUN tar -zxvf jdk-8u151-linux-x64.tar.gz -C /opt/java
RUN ln -s /opt/java/jdk1.7.0_80 /opt/java/jdk
RUN echo "export JAVA_HOME=/opt/java/jdk" >> /etc/profile \
    && echo "exprot PATH=$JAVA_HOME/bin:$PATH" >> /etc/profile \
	&& echo "export CLASSPATH=.:$JAVA_HOME/jre/lib/rt.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar" >> /etc/profile
RUN mkdir -p /opt/tomcat
ADD apache-tomcat-8.5.24.tar.gz /root
RUN tar -xvf apache-tomcat-8.5.24.tar.gz -C /opt/tomcat/
RUN ln -s /opt/tomcat/apache-tomcat-8.5.24 /opt/tomcat/tomcat8.5
WORKDIR /opt/tomcat/tomcat8.5
CMD startup.sh