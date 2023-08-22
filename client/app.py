import grpc
import car_pb2
import car_pb2_grpc

def fetch_data_from_server(index_name):
    try:
        server_address = 'localhost:50051'  
        channel = grpc.insecure_channel(server_address)
        stub = car_pb2_grpc.CarServiceStub(channel)
        
        print("Fetching data from gRPC server...")
        request = car_pb2.GetCarsRequest(index_name=index_name)
        response = stub.GetCars(request)
        
        cars_data = []
        for car in response.cars:
            cars_data.append({
                'title': car.title,
                'price': car.price,
                'place': car.place,
                'engine_capacity': car.engine_capacity,
                'registered_in': car.registered_in,
                'image': car.image
            })
        
        return cars_data
    except Exception as e:
        print("Error fetching data:", e)

if __name__ == '__main__':
    index_name = "pak-string"  
    fetched_data = fetch_data_from_server(index_name)
    print(fetched_data)
