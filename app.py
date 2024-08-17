from flask import Flask, abort,jsonify,request

app = Flask(__name__)

Task_model = [ {"id": 1, "title": "UI/UX", "description": 'first step', "status": 'Done', "created_at" : '2024-08-01',"updated_at" : '2024-08-17' },
             {"id": 2, "title": "Development", "description": 'develop the product', "status": 'Dev-ready', "created_at" : '2024-08-01',"updated_at" : '2024-08-17'},
             {"id": 3, "title": "Testing", "description": 'test it', "status": 'staging', "created_at" : '2024-08-01',"updated_at" : '2024-08-17'} ]

@app.route("/getTasks", methods=['GET'])
def getAllTasks():
    return jsonify(Task_model)

@app.route("/getTasksById/<int:Task_modelId>", methods=['GET'])
def getTasksById(Task_modelId):
    for task in Task_model:
        if task['id'] == Task_modelId:
            return jsonify(task)
    return jsonify({"error": "Task Id not found"}), 404

@app.route("/addTask", methods=['POST'])
def add():
    # request and response
    task_new = request.json
    Task_model.append(task_new)
    return jsonify({ "Tasks" : task_new}), 201


@app.route("/UpdateTasksById/<int:Task_modelId>", methods=['GET'])
def updateTasksById(Task_modelId):
            task_update = [{"id": 2, "title": "Presales", "description": 'second step', "status": 'dev', "created_at" : '2024-08-01',"updated_at" : '2024-08-17'  }]
            return jsonify(task_update), 200



@app.route("/DeleteTasksById/<int:Task_modelId>", methods=['DELETE'])
def delete_item(Task_modelId):
    # Check if the item exists in the dictionary
    if Task_modelId in Task_model:
        del Task_model[Task_modelId]
        return jsonify({"message": f"Item {Task_modelId} deleted successfully"}), 200
    else:
        # If the item doesn't exist, return a 404 error
        abort(404, description="Task id not found")


if __name__ == '__main__':
    app.run(debug=True)



