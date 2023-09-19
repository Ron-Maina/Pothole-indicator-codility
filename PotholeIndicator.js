function PotholeIndicator(R){
    let sub_arr = []
    let portholeIndicator = 0

    function calculate(){
        let RK = ((Math.max.apply(null, sub_arr)) * (sub_arr.length))
        if (RK > portholeIndicator){
            portholeIndicator = RK
        }
        sub_arr = []
    }
    for (let num of R){
        if (num !== 0){
            sub_arr.push(num)
        }
        else{
            console.log(sub_arr)
            calculate()
        }
    }
    if (sub_arr.length > 1){
        console.log(sub_arr)
        calculate()
    }
    console.log(portholeIndicator)
}
PotholeIndicator([9, 8, 7, 0, 0, 0, 2, 3, 6, 4])