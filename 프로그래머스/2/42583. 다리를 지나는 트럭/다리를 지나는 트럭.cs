using System;
using System.Collections.Generic;
public class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int passedTime = 0;
        int remainWeight = weight;
        Queue<int> readyQ = new Queue<int>(truck_weights);
        // key : weight, value : enqueueTime 
        Queue<KeyValuePair<int, int>> passingQ = new Queue<KeyValuePair<int, int>>();
        
        while(readyQ.Count > 0 || passingQ.Count > 0)
        {
            Console.WriteLine($"passedTime : {passedTime} remainWeight : {remainWeight} readyQ.Count : {readyQ.Count} passingQ.Count : {passingQ.Count} remainWeight : {remainWeight}");
            if(readyQ.TryPeek(out var truckWeight) && remainWeight > truckWeight)
            {
                remainWeight -= truckWeight;
                readyQ.Dequeue();
                passingQ.Enqueue(new KeyValuePair<int, int>(truckWeight, passedTime));
            }
            ++passedTime;
            if(passingQ.TryDequeue(out var passingTruck))
            {
                Console.WriteLine($"?? passingTruck.Value {passingTruck.Value} passedTime : {passedTime} bridge_length : {bridge_length}");
                if(bridge_length <= (passedTime - passingTruck.Value))
                {
                    remainWeight += passingTruck.Key;
                    passingQ.Dequeue();    
                }
                
            }
            if(passedTime > 10)
                break;
        }
        ++passedTime;
        return passedTime;
    }
}