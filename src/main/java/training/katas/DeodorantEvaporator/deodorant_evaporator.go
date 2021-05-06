package DeodorantEvaporator

func Evaporator(content float64, evapPerDay int, threshold int) int {
	var nthDay = 0
	var absoluteThreshold = content * float64(threshold) / 100
	for {
		nthDay += 1
		content *= float64((100.0 - float64(evapPerDay)) / 100.0)
		if content < absoluteThreshold {
			break
		}
	}
	return nthDay
}
