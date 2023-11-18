package DeodorantEvaporator

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

const (
	Epic    = "epic Problems"
	Feature = "feature Easy"
	Story   = "story Maximum subarray"
)

// https://towardsdatascience.com/use-environment-variable-in-your-next-golang-project-39e17c3aaa66
// use godot package to load/read the .env file and
// return the value of the key
func goDotEnvVariable(key string) string {

	// load .env file
	err := godotenv.Load("variables.env")

	if err != nil {
		log.Fatalf("Error loading .env file")
	}

	return os.Getenv(key)
}

func dotest(content float64, evapPerDay int, threshold int, exp int) {
	var ans = Evaporator(content, evapPerDay, threshold)
	Expect(ans).To(Equal(exp))
}

var _ = Describe("Tests Evaporator", func() {

	It("should handle basic cases", func() {
		dotest(10, 10, 10, 22)
		dotest(10, 10, 5, 29)
		dotest(100, 5, 5, 59)

	})
})

func TestStepDeodorantEvaporator(t *testing.T) {
	dotenv := goDotEnvVariable("ALLURE_RESULTS_PATH")
	allure.Test(t,
		allure.Epic(Epic),
		allure.Feature(Feature),
		// // allure.Story(Story),
		// allure.Description("test Maximum subarray 01"),
		allure.Action(func() {
			Expect(Evaporator(10, 10, 10)).To(Equal(22))
			Expect(Evaporator(10, 10, 5)).To(Equal(29))
			Expect(Evaporator(100, 5, 5)).To(Equal(59))
		}))
}
