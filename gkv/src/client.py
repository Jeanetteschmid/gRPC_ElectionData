import grpc
import electiondata_pb2
import electiondata_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = electiondata_pb2_grpc.ElectiondataStub(channel)

    request = electiondata_pb2.MessageRequest(regionID="123")
    response = stub.GetElectionData(request)

    print("Received: ", response)

if __name__ == '__main__':
    run()