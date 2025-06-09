# asynchronous programming
# is a programming paradigm where long running task
# can be run in the background, separate from
# main application. Once the long running task
# finishes, then we will be notified so that
# we can process the results
#
# asyncio is a library that allow you
# to execute coroutines in an asynchronous fashion
# using concurrency model or single-threaded event loop
#
# asynchronous, event loop is good for CPU or I/O bound
# 
#
# in the field of concurrent programming, there are a few
# different concepts that we need to understand:
#
# 1. Concurrency
#       concurrency is the concept when there are two tasks
# that are happening at the same time. When two tasks are 
# working at the same time, it is happening concurrently.
# If a baker is preheating the over and mixing flour and sugar,
# it means thata the baker is concurrently executing two tasks
# at the same time. Switching between tasks is concurrent behaviour.
# 
# Baker -> Mix Flour
#       -> PreHeat Oven [ X X X - - -]
#       -> Boil Water   [ X X X X X -]
#
# 2. Parallelism
#       parallelism on the other hand is when there are two
# or more tasks that are happening concurrently and executing.
# at the same time. In the scenario of a baker, parallelism mean
# that there are two baker.
# 
# Baker -> Mix Flour
# Baker -> PreHeat Oven
#       -> Boil Water 
#
# Main differences
#       One of the main differences is the state. Concurrency have one active
# state, whereas paralellism have two active state. If we picture this over
# in an application.
# 
# Concurrency is switching - Applications 1 (one active)
#                          - Applications 2
# 
# Parallelism is Actively - Application 1 ( running )
#                         - Application 2 ( running )
#
# 3. Multitasking
#       multitasking is when you are working on multi task at the same time
# in this model, there are normally two types of multi tasking
#       A) preemptive multitasking
# is a concept where the OS (kernel) decides how long each task runs.
# interrupting task when needed to give other tasks a run. It ensures
# fair CPU time and responsiveness.
#
#       B) cooperative multitasking
# instead of relying on the OS, we explicitly code in our application
# where we can let tasks run. We code points in the application
# and cooperate.
# 
# 4. One Core vs Multi Cores
# in a machine with one core, we can achieve concurrency,
# since you can do preemptive multitasking and multi task
# between the one core of execution
#
# however, a machine with two cores allow you to do parallelism
# it means that you can execute two or more tasks aat the same
# time. Multi Cores cpu allow the running of two tasks together
# 
# asyncio ---- ####
# under the hood asyncio uses cooperative multitasking for concurrency
# it will execute a code and mark the code, while we wait for the results to 
# return in background. It gives a form of concurrency because multi tasks started
# however, they are running concurrently and not in parallel.
#
# context switching 
# in the event where an OS need to switch between a process and a thread
# it triggers what you called a context switching
#
# context switches are intensive operations since the os need to save
# information about running process or thread to be able to reload
# 

#
# coroutines
import asyncio
import io
import time

def main():
    hello_world()

# coroutine is the basics of multitasking, cooperative multitasking.
# it allows you to perform concurrent programming.
# co routine is not parallel programming since it basically
# let the function execute and come back to it later


async def hello_coroutine() -> None:
    print("Hello World")


async def hello_world() -> None:
    print("sleeping")
    time.sleep(2)
    return "hello world"


if __name__=="__main__":
    main()