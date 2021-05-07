package training.katas.HumanReadableDurationFormat

import org.junit.Ignore
import kotlin.test.assertEquals
import org.junit.Test

class TimeFormatterKtTest {
    @Ignore
    @Test
    fun testFormatDurationExamples() {
        // Example Test Cases
        assertEquals("1 second", TimeFormatter.formatDuration(1))
        assertEquals("1 minute and 2 seconds", TimeFormatter.formatDuration(62))
        assertEquals("2 minutes", TimeFormatter.formatDuration(120))
        assertEquals("1 hour", TimeFormatter.formatDuration(3600))
        assertEquals("1 hour, 1 minute and 2 seconds", TimeFormatter.formatDuration(3662))
    }
}
