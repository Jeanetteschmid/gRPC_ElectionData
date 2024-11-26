import grpc
from concurrent import futures
import electiondata_pb2
import electiondata_pb2_grpc
import time

class ElectiondataServicer(electiondata_pb2_grpc.ElectiondataServicer):
    def GetElectionData(self, request, context):
        election = electiondata_pb2.ElectionData(
            regionID="123",
            regionName="Sample Region",
            regionAddress="123 Main St",
            regionPostalCode="12345",
            federalState="Sample State",
            timestamp="2024-11-26 14:31:56"
        )

        party = electiondata_pb2.Party(
            partyID="SPOE",
            amountVotes=1000
        )

        party2 = electiondata_pb2.Party(
            partyID="FPOE",
            amountVotes=800
        )

        election.countingData.extend([party])
        election.countingData.extend([party2])


        return electiondata_pb2.MessageResponse(responseData=election)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    electiondata_pb2_grpc.add_ElectiondataServicer_to_server(ElectiondataServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()