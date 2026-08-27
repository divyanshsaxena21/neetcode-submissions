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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        long num1 = 0;
        long place = 1;

        while(l1 != NULL){
            num1 += l1->val * place;
            place *= 10;
            l1 = l1->next;
        }

        long num2 = 0;
        place = 1;

        while(l2 != NULL){
            num2 += l2->val * place;
            place *= 10;
            l2 = l2->next;
        }

        num1 = num1 + num2;

        if (num1 == 0)
            return new ListNode(0);

        ListNode* newHead = NULL;
        ListNode* tail = NULL;

        while(num1){
            long r = num1 % 10;
            num1 = num1 / 10;

            ListNode* newNode = new ListNode(r);

            if (newHead == NULL){
                newHead = newNode;
                tail = newNode;
            }
            else{
                tail->next = newNode;
                tail = tail->next;
            }
        }

        return newHead;
    }
};
