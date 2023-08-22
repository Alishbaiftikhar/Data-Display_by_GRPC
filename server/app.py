from concurrent import futures
import grpc
import car_pb2
import car_pb2_grpc
from elasticsearch import Elasticsearch

class CarService(car_pb2_grpc.CarServiceServicer):
    def GetCars(self, request, context):
        index_name = request.index_name
        
        print(f"Fetching data from Elasticsearch for index {index_name}...")
        print("Fetching data from Elasticsearch...")
        es_host = 'localhost'
        es_port = 9200
        es = Elasticsearch(hosts=[{'host': es_host, 'port': es_port}])
        print("......",es)
        
        query = {
            "query": {
                "match_all": {}
            },
            "size": 30,
        }
        resp = es.search(index=index_name, body=query)
        hits = resp['hits']['hits']
        print(resp)
        print(hits)
        cars_data = []
        for hit in hits:
            get_data = hit['_source']
            # import pdb;pdb.set_trace()
            car = car_pb2.Car(
                title=get_data['title'],
                price=get_data['price'],
                # price=get_data.get('prices', "")
                place=get_data['place'],
                engine_capacity=get_data['engine-capacity'],
                registered_in=get_data['Registered In'],
                image=get_data['image'][0]
            )
            cars_data.append(car)
        print(cars_data)
        
        return car_pb2.GetCarsResponse(cars=cars_data)

def serve():
    port = 50051
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    car_pb2_grpc.add_CarServiceServicer_to_server(CarService(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print(f"Server started, listening on port {port}")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
