new Vue({
    el: "#app",
    data: {
        tests: [
            { name: "Test 1", myString: "xxxy", maxRepeat: 2, testCompleted: false, myResult: "" },
            { name: "Test 2", myString: "xxyy", maxRepeat: 1, testCompleted: false, myResult: "" },
            { name: "Test 3", myString: "xxxxyyyyxx", maxRepeat: 1, testCompleted: false, myResult: "" },
            { name: "Test 4", myString: "aaaabbbbccccdddd", maxRepeat: 1, testCompleted: false, myResult: "" },
            { name: "Test 5", myString: "aaaabbbbccccdddd", maxRepeat: 2, testCompleted: false, myResult: "" },
            { name: "Test 6", myString: "aaaabbbbccccdddd", maxRepeat: 3, testCompleted: false, myResult: "" },
        ]
    },
    methods: {
        formatString: function (test) {
            var { maxRepeat, myResult, myString, testCompleted } = test
            let count = 0
            for (let i = 0; i < myString.length - 1; i++) {
                if (myString[i] == myString[i + 1]) {
                    count++
                    if (count <= maxRepeat) { myResult += myString[i] }
                } else {
                    if (count < maxRepeat) {
                        myResult += myString[i]

                        count = 0
                    }
                    myResult += myString[i + 1]


                }
            }
            console.log(myResult)
        }
    }
})