#!/usr/bin/env python3

from aws_cdk import core

from my_first_cdk_proj.my_first_cdk_proj_stack import MyFirstCdkProjStack


app = core.App()
MyFirstCdkProjStack(app, "my-first-cdk-proj")

app.synth()
