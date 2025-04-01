document.addEventListener("DOMContentLoaded", function (){
    
    const urlParams = new URLSearchParams(window.location.search);
    const fees = urlParams.get("fees").toString();
    console.log('fees is: ', fees);
    if (isNaN(fees) || fees <= 0) {
        alert("Invalid fees amount. Please try again.");
        return;
    }
    
    const payButton = document.getElementById("pay-button");
    if(payButton){
        payButton.addEventListener("click", function(event) {
            event.preventDefault();
            //Razorpay payment integration
            const amountInPaise = fees * 100;  //razorpay requires the amount in paise
            const options = {
                key: "rzp_test_Am8Zi1bznoNdxl",
                amount: amountInPaise,
                currency: "INR",
                name: "GSMCOE",
                description: "Event Registration Payment",
                handler: function(response){
                    document.querySelector(".form-items").submit();
                    
                },
                prefill: {
                    name: document.getElementById("id_full_name")?.value || "",
                    email: document.getElementById("id_email")?.value || "",
                    phone: document.getElementById("id_contact_number")?.value || "",
                },
                theme: {
                    color: "#d84e55",
                }
            }

            const rzp = new Razorpay(options);
            rzp.open();

            rzp.on("payment.failed", function(response){
                // handle payment failure
                alert("Payment failed. Please try again. Error: " + response.error.description)
            })

        })
    }
})