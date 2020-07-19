from flask import Flask, render_template, url_for, request
from flask_restful import reqparse, abort, Api, Resource
import cv2


c