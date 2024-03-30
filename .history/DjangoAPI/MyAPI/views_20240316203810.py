from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import csv,os,datetime,json

def set_cors_headers(response):
  response['Access-Control-Allow-Origin'] = '*'
  response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'  # Add allowed methods
  response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'  # Add allowed headers
  return response
# Create your views here.

def parse_csv_from_json(csv_data):
    # Parse CSV data from the JSON payload
    csv_list = csv_data.splitlines()
    csv_reader = csv.reader(csv_list)
    csv_data = []
    for row in csv_reader:
        csv_data.append(row)
    return csv_data

@csrf_exempt
def prediction(request):
     
    if request.method =="POST":
        data_str = request.body .decode('utf-8')
        json_data = json.loads(data_str)

        # Extract the filedata
        filedata = json_data.get('file', '')
        try:
            directory = "/Users/Dell/Desktop/django/"
            current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            if not os.path.exists(directory):
             os.makedirs(directory)
            filename = f"data_{current_timestamp}.csv"
    #     with open(os.path.join(directory, filename), "w", newline='') as f:
    #         writer = csv.writer(f)
    #         writer.writerows(parsed_data)
    #   if 'file' not in request.json:
    #    print(request.body)
    #   csv_data = request.json['file']
    #   try:
    #    parsed_data = parse_csv_from_json(csv_data)
        
    #     # Export CSV data to a file named "raw.csv" in a directory
    #     directory = "/Users/Dell/Desktop/django/"
    #     if not os.path.exists(directory):
    #         os.makedirs(directory)
        
    #     # Get current timestamp
    #     current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    #     # Generate filename with current timestamp
    #     filename = f"data_{current_timestamp}.csv"
    #     with open(os.path.join(directory, filename), "w", newline='') as f:
    #         writer = csv.writer(f)
    #         writer.writerows(parsed_data)
        
        return JsonResponse({'message': 'Successfully received CSV'})
    #   except Exception as e:
        # return JsonResponse({'error': str(e)}), 400
    # else:
        #  return JsonResponse({'error'}), 400