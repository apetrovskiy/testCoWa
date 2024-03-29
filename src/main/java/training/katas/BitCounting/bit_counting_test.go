package BitCounting

import (
	// . "codewarrior/kata"
	"github.com/dailymotion/allure-go"
	"github.com/joho/godotenv"
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
	"log"
	"os"
	"testing"
)

var _ = Describe("CountBits()", func() {
	It("basic tests", func() {
		Expect(CountBits(0)).To(Equal(0))
		Expect(CountBits(4)).To(Equal(1))
		Expect(CountBits(7)).To(Equal(3))
		Expect(CountBits(9)).To(Equal(2))
		Expect(CountBits(10)).To(Equal(2))
	})
})

const (
	Epic    = "epic Training"
	Feature = "feature Katas"
	Story   = "story Bit Counting"
)

// https://towardsdatascience.com/use-environment-variable-in-your-next-golang-project-39e17c3aaa66
// use godot package to load/read the .env file and
// return the value of the key
func goDotEnvVariable(key string) string {

	// load .env file
	err := godotenv.Load("../../../../../../variables.env")

	if err != nil {
		log.Fatal(err)
		log.Fatalf("Error loading .env file")
	}

	return os.Getenv(key)
}

func dotest(input uint, exp int) {
	var ans = CountBits(input)
	Expect(ans).To(Equal(exp))
}

func TestStepBitCounting(t *testing.T) {

	dotenv := goDotEnvVariable("ALLURE_RESULTS_PATH")
	allure.Test(t,
		allure.Epic(Epic),
		allure.Feature(Feature),
		// // allure.Story(Story),
		// allure.Description("test Maximum subarray 01"),
		allure.Action(func() {
			Expect(CountBits(0)).To(Equal(0))
			Expect(CountBits(4)).To(Equal(1))
			Expect(CountBits(7)).To(Equal(3))
			Expect(CountBits(9)).To(Equal(2))
			Expect(CountBits(10)).To(Equal(2))
		}))

}
