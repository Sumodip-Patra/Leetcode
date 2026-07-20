/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *dummy= new ListNode(0);
        dummy->next=head;
        ListNode *ref= dummy;
        ListNode *main= dummy;

        //moving the ref pointer to the first n node
        for(int i=0;i<=n;i++){
            ref=ref->next;
        }        

        
        
        // both will moving till ref-> next != NULL while maintaining the len-k+1 distance
        while(ref!=NULL){
            main=main->next;
            ref=ref->next;
        }
        // moving main so that it can remove the node of the nth last position
        main->next= main->next->next;
        return dummy->next;

    }
};