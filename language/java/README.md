# New java application

## Install openjdk java language

java environment tools

```bash
brew install jenv
```

integrate with zshell, ```vi ~/.zshrc```

```markdown
plugins=(
    .
    .
    .
    jenv
    .
)
```

java 11 LTS version with openjdk hotspot

```bash
brew tap AdoptOpenJDK/openjdk
brew install --cask adoptopenjdk11
```

move project directory and setting jenv

```bash
jenv local 11
```

Run

```
➜  java git:(master) ✗ java -version
openjdk version "11.0.10" 2021-01-19
OpenJDK Runtime Environment AdoptOpenJDK (build 11.0.10+9)
OpenJDK 64-Bit Server VM AdoptOpenJDK (build 11.0.10+9, mixed mode)

 java git:(master) ✗ jshell
|  Welcome to JShell -- Version 11.0.10
|  For an introduction type: /help intro

jshell>
```

References

* <https://adoptopenjdk.net/>

## Immediately Run with java command

```java
package javatutorial;

class HelloWorld{
    public static void main(String[] args) {
        System.out.println("hello world");
    }
}
```

```shell
java HelloWorld.java
hello world
```

## Setting gradle

### gradle wrapper

prepare gradle utility

```bash
brew install gradle
```

create ```settings.gradle``` file and project name

```
rootProject.name = 'til'
```

carete gradle wrapper

```bash
gradle wrapper

./gradlew
Downloading https://services.gradle.org/distributions/gradle-7.2-bin.zip
..........10%...........20%...........30%...........40%...........50%...........60%...........70%...........80%...........90%...........100%

> Task :help

Welcome to Gradle 7.2.

To run a build, run gradlew <task> ...

To see a list of available tasks, run gradlew tasks

To see a list of command-line options, run
```

### Application code

Application running for main code
Create directory ```src/main/java/til``` and file ```Application.java```

```java
package til;

public class Application {
    public static void main(String[] args) {
        System.out.println("Welcome, This is Tody I Learn Java Applcation.");
        return;
    }
}
```

### Build

Building to create ```build.gradle`` file and setting plugin java

```
apply plugin: 'java'
```

```bash
./gradlew build
executing gradlew instead of gradle

BUILD SUCCESSFUL in 1s
2 actionable tasks: 2 executed

ls build  ### result files fo build
classes   generated libs      tmp
```

### Run

Application running for gradle for setting  ```build.gradle```

```
apply plugin: 'application'
mainClassName = 'til.Application'
```

Run application

```shell
$ ./gradlew run

> Task :run
Welcome, This is Tody I Learn Java Applcation.

BUILD SUCCESSFUL in 831ms
2 actionable tasks: 1 executed, 1 up-to-date
```

### Dependency
Edit ```build.gradle```

```
group = 'til'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = 1.8

repositories {
	mavenCentral()
}

dependencies {
}
```

References

* <https://docs.gradle.org/current/userguide/gradle_wrapper.html>
